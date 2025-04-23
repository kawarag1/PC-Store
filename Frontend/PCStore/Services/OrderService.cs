using Newtonsoft.Json;
using PCStore.Schemas;
using PCStore.Schemas.DTO;
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
        private const string CheckOrdersUrl = "https://pcstore.space/v1/order/check";


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

        public async Task<List<OrderDTO>> CheckOrder()
        {
            try
            {
                var request = new HttpRequestMessage(HttpMethod.Get, CheckOrdersUrl);
                var handler = new AuthentificatedHttpClientService(
                        new UserService(),
                        new HttpClientHandler());

                var _client = new HttpClient(handler);

                var _response = _client.SendAsync(request, new CancellationToken());
                var response = await _response;

                if (response.IsSuccessStatusCode)
                {
                    string responseJson = await response.Content.ReadAsStringAsync();
                    var Orders = JsonConvert.DeserializeObject<List<OrderDTO>>(responseJson);

                    return Orders;
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

        public async Task<List<ProductItemModel>> OrderList(List<OrderDTO> orders)
        {
            try
            {
                var result = new List<ProductItemModel>();
                var productDictionary = new Dictionary<string, ProductItemModel>();

                foreach (var basket in orders)
                {
                    void ProcessProduct<T>(T product, Func<T, ProductItemModel> createModel) where T : class
                    {
                        if (product == null) return;

                        dynamic dynamicProduct = product;
                        string key = $"{dynamicProduct.Id}_{dynamicProduct.Article}"; 

                        if (productDictionary.TryGetValue(key, out var existingProduct))
                        {
                            existingProduct.Counter++;
                        }
                        else
                        {
                            var newProduct = createModel(product);
                            productDictionary.Add(key, newProduct);
                        }
                    }

                    ProcessProduct(basket.Cpus, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Gpus, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Rams, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Motherboards, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.PuS, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Cases, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.HDDs, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.SSDs, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.M2SSds, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Vents, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(basket.Coolers, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });


                }
                result.AddRange(productDictionary.Values);
                return result;
            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return null;
            }
        }
    }
}
