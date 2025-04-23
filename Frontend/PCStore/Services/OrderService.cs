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
                bool result = true;

                var handler = new AuthentificatedHttpClientService(
                   new UserService(),
                   new HttpClientHandler());

                using (var _client = new HttpClient(handler))
                {
                    foreach (var item in products)
                    {
                        BasketRequest _item = new BasketRequest();
                        _item.id = item.Id;
                        _item.article = item.Article;
                        if (item.Cost != null)
                        {
                            _item.cost = item.Cost;
                        }
                        string json = JsonConvert.SerializeObject(_item);
                        var content = new StringContent(json, Encoding.UTF8, "application/json");

                        if (item.Counter > 0)
                        {
                            for (int i = 0; i < item.Counter; i++)
                            {
                                var request = new HttpRequestMessage(HttpMethod.Post, CreateFastOrderUrl)
                                {
                                    Content = content
                                };
                                var response = await _client.SendAsync(request, new CancellationToken());


                                BasketService service = new BasketService();
                                List<ProductItemModel> list = new List<ProductItemModel>();
                                list.Add(item);
                                await service.DeleteOneFromBasket(list);
                                if (!response.IsSuccessStatusCode)
                                {
                                    result = false;
                                    break;
                                }
                            }
                        }
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
