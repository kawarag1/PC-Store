using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PCStore.Services;
using System.Net;
using System.Diagnostics;

namespace PCStore.Services
{
    public class AuthentificatedHttpClientService: DelegatingHandler
    {
        private readonly UserService _userService;

        public AuthentificatedHttpClientService(UserService userService, HttpClientHandler handler)
            :base (handler)
        {
            _userService = userService;
        }

        protected override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken token)
        {
            var response = await SendWithTokenAsync(request, token);

            if (response.StatusCode == HttpStatusCode.Unauthorized)
            {
                bool tokenref = await _userService.RefreshTokenAsync();
                if (tokenref)
                {
                    response = await SendWithTokenAsync(request, token);
                }
                else
                {

                }
            }

            return response;
        }


        private async Task<HttpResponseMessage> SendWithTokenAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
        {
            try
            {
                string accessToken = await SecureStorage.GetAsync("access_token");
                if (!string.IsNullOrEmpty(accessToken))
                {
                    request.Headers.Authorization =
                        new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken);
                }
                return await base.SendAsync(request, cancellationToken);
            }
            catch (Exception ex)
            {
                Debug.WriteLine($"SecureStorage error: {ex.Message}");
                return await base.SendAsync(request, cancellationToken);
            }
            
        }
    }
}
