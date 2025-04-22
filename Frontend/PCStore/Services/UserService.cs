using System;
using System.Collections.Generic;
using System.Linq;
using System.Net.Http.Headers;
using System.Text;
using Newtonsoft.Json;
using System.Threading.Tasks;

using PCStore.Schemas;

namespace PCStore.Services
{
    public class UserService
    {
        private const string AuthUrl = "https://pcstore.space/v1/user/authtorization";
        private const string RefreshUrl = "https://pcstore.space/v1/user/refresh";
        private const string GetProfileUrl = "https://pcstore.space/v1/user/get_profile";
        private const string RegUserUrl = "https://pcstore.space/v1/user/registration";
        private AuthentificatedHttpClientService authHttpClientService;

        

        public async Task<bool> Auth(string login, string pwd, HttpClient _client)
        {
            if (string.IsNullOrEmpty(login) || string.IsNullOrEmpty(pwd))
            {
                await Shell.Current.DisplayAlert("Ошибка", "Логин/пароль не могут быть пустыми", "OK");
                return false;
            }

            var requestData = new Dictionary<string, string>
            {   
                {"username", login },
                {"password", pwd }
            };

            var encodedData = new FormUrlEncodedContent(requestData);

            HttpResponseMessage response = await _client.PostAsync(AuthUrl, encodedData);

            string responseJson = await response.Content.ReadAsStringAsync();


            if (response.IsSuccessStatusCode)
            {
                TokenSchema? tokens = JsonConvert.DeserializeObject<TokenSchema>(responseJson);

                await SecureStorage.SetAsync("access_token", tokens.AccessToken);
                await SecureStorage.SetAsync("refresh_token", tokens.RefreshToken);

                await SecureStorage.SetAsync("login", login);
                await SecureStorage.SetAsync("password", pwd);

                return true;
            }
            else
            {
                var error = JsonConvert.DeserializeObject(responseJson);
                Shell.Current.DisplayAlert("Ошибка", error.ToString(), "OK");
                return false;
            }

        }

        public async Task<bool> RefreshTokenAsync()
        {
            try
            {
                string refreshToken = await SecureStorage.GetAsync("refresh_token");
                if (string.IsNullOrEmpty(refreshToken))
                {
                    return false;
                }
                else
                {
                    HttpClient _client = new HttpClient();
                    _client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", refreshToken);

                    HttpResponseMessage response = await _client.GetAsync(RefreshUrl);


                    if (response.IsSuccessStatusCode)
                    {
                        string responseJson = await response.Content.ReadAsStringAsync();
                        var tokens = JsonConvert.DeserializeObject<TokenSchema>(responseJson);
                        await Shell.Current.DisplayAlert("Ошибка", $"{tokens}", "OK");

                        await SecureStorage.SetAsync("access_token", tokens.AccessToken);
                        return true;
                    }
                    else
                    {
                        return false;
                    }
                }
            }
            catch (Exception ex)
            {
                //await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return false;
            }
            
        }

        public async Task Logout()
        {
            SecureStorage.Remove("access_token");
            SecureStorage.Remove("refresh_token");
        }


        public async Task<UserSchema> GetProfile()
        {
            try
            {
                var request = new HttpRequestMessage(HttpMethod.Get, GetProfileUrl);
                var handler = new AuthentificatedHttpClientService(
                        new UserService(),
                        new HttpClientHandler());

                var _client = new HttpClient(handler);

                var response = await _client.SendAsync(request, new CancellationToken());
                
                if (response.IsSuccessStatusCode)
                {
                    var Jsondata = await response.Content.ReadAsStringAsync();
                    var data = JsonConvert.DeserializeObject<UserSchema>(Jsondata);
                    return data;
                }
                else
                {
                    return null;
                }
            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return null;
            }
            
        }


        public async Task<bool> RegUser(UserSchema user, HttpClient _client)
        {
            try
            {
                if (string.IsNullOrEmpty(user.Login) || string.IsNullOrEmpty(user.Password) || string.IsNullOrEmpty(user.Email))
                {
                    await Shell.Current.DisplayAlert("Ошибка", "Логин, пароль и электронная почта не должны быть пустыми", "OK");
                    return false;
                }

                var JsonData = JsonConvert.SerializeObject(user);
                var content = new StringContent(JsonData, Encoding.UTF8, "application/json");

                HttpResponseMessage response = await _client.PostAsync(RegUserUrl, content);

                if (response.IsSuccessStatusCode)
                {
                    await Auth(user.Login, user.Password, _client);
                    return true;
                }
                else
                {
                    return false;
                }

            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return false;
            }
        }

        public async static Task<bool> IsAuth()
        {
            string access_token = await SecureStorage.GetAsync("access_token");

            if (access_token == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }
    }
}
