using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using PCStore.Services;
using System.Net;

namespace PCStore.Services
{
    public class AuthHttpClientService: HttpClient
    {
        private static UserService _userService;

        public AuthHttpClientService(UserService userService)
        {
            _userService = userService;
        }

        public override async Task<HttpResponseMessage> SendAsync(HttpRequestMessage request, CancellationToken token)
        {
            var response = await SendWithTokenAsync(request, token);

            if (response.StatusCode == HttpStatusCode.Unauthorized)
            {
                if (await _userService.RefreshTokenAsync(new HttpClient()))
                {
                    response = await SendWithTokenAsync(request, token);
                }
            }

            return response;
        }


        private async Task<HttpResponseMessage> SendWithTokenAsync(
        HttpRequestMessage request,
        CancellationToken cancellationToken)
        {
            string accessToken = await SecureStorage.GetAsync("access_token");
            if (!string.IsNullOrEmpty(accessToken))
            {
                request.Headers.Authorization =
                    new System.Net.Http.Headers.AuthenticationHeaderValue("Bearer", accessToken);
            }
            return await base.SendAsync(request, cancellationToken);
        }



    }
}
