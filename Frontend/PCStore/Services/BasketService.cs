using Newtonsoft.Json;
using PCStore.Schemas;
using PCStore.Schemas.DTO;
using PCStore.Schemas.Request;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography;
using System.Text;
using System.Threading.Tasks;

namespace PCStore.Services
{
    public class BasketService
    {
        private const string CheckBasketUrl = "https://pcstore.space/v1/basket/check";
        private const string DeleteOneFromBasketUrl = "http://pcstore.space/v1/basket/delete_one_from_basket";
        private const string AddToBasketUrl = "https://pcstore.space/v1/basket/add_to_basket";


        public async Task<bool> AddToBasket(List<ProductItemModel> products)
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
                        string json = JsonConvert.SerializeObject(_item);
                        var content = new StringContent(json, Encoding.UTF8, "application/json");

                        var request = new HttpRequestMessage(HttpMethod.Post, AddToBasketUrl)
                        {
                            Content = content
                        };
                        var response = await _client.SendAsync(request, new CancellationToken());
                        if (!response.IsSuccessStatusCode)
                        {
                            result = false;
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


        public async Task<List<BasketDTO>> CheckBasket()
        {
            try
            {
                var request = new HttpRequestMessage(HttpMethod.Get, CheckBasketUrl);
                var handler = new AuthentificatedHttpClientService(
                        new UserService(),
                        new HttpClientHandler());

                var _client = new HttpClient(handler);

                var _response = _client.SendAsync(request, new CancellationToken());
                var response = await _response;

                if (response.IsSuccessStatusCode)
                {
                    string responseJson = await response.Content.ReadAsStringAsync();
                    var Basket = JsonConvert.DeserializeObject<List<BasketDTO>>(responseJson);

                    return Basket;
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


        public async Task<bool> DeleteOneFromBasket(List<ProductItemModel> products)
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
                        string json = JsonConvert.SerializeObject(_item);
                        var content = new StringContent(json, Encoding.UTF8, "application/json");

                        var request = new HttpRequestMessage(HttpMethod.Delete, DeleteOneFromBasketUrl)
                        {
                            Content = content
                        };
                        var response = await _client.SendAsync(request, new CancellationToken());
                        if (!response.IsSuccessStatusCode)
                        {
                            result = false;
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


        public async Task<bool> DeleteOneFromBasket(BasketRequest product)
        {
            try
            {
                var request = new HttpRequestMessage(HttpMethod.Delete, DeleteOneFromBasketUrl);
                string json = JsonConvert.SerializeObject(product);
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

        public async Task<List<ProductItemModel>> BasketList(List<BasketDTO> baskets)
        {
            try
            {
                var result = new List<ProductItemModel>();
                var productDictionary = new Dictionary<string, ProductItemModel>();

                foreach (var basket in  baskets)
                {
                    void ProcessProduct<T>(T product, Func<T, ProductItemModel> createModel) where T : class
                    {
                        if (product == null) return;

                        dynamic dynamicProduct = product;
                        string key = $"{dynamicProduct.Id}_{dynamicProduct.Article}"; // Уникальный ключ по ID и артикулу

                        if (productDictionary.TryGetValue(key, out var existingProduct))
                        {
                            // Если товар уже есть - увеличиваем счетчик
                            existingProduct.Counter++;
                        }
                        else
                        {
                            // Если товара нет - добавляем новый
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
