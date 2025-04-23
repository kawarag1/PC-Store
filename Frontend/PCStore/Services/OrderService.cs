using Newtonsoft.Json;
using PCStore.Schemas;
using PCStore.Schemas.Request;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.CompilerServices;
using System.Text;
using System.Threading.Tasks;

namespace PCStore.Services
{
    class OrderService
    {
        private const string CreateFastOrderUrl = "https://pcstore.space/v1/order/create_fast_order";


        public async Task<bool> CreateOrder(List<ProductItemModel> products)
        {
            try
            {
                bool result = false;

                var request = new HttpRequestMessage(HttpMethod.Post, CreateFastOrderUrl);
                foreach (var item in products)
                {
                    BasketRequest _item = new BasketRequest();
                    _item.id = item.Id;
                    _item.article = item.Article;
                    string json = JsonConvert.SerializeObject(_item);
                    var content = new StringContent(json, Encoding.UTF8, "application/json");
                    request.Content = content;
                    var handler = new AuthentificatedHttpClientService(
                        new UserService(),
                        new HttpClientHandler());

                    var _client = new HttpClient(handler);

                    var _response = _client.SendAsync(request, new CancellationToken());
                    var response = await _response;
                    if (response.IsSuccessStatusCode)
                    {
                        result = true;
                    }
                    else
                    {
                        result = false;
                    }
                }
                return result;

            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return false;
            }
        }
    }
}
