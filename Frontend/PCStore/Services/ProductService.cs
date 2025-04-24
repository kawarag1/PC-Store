using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using PCStore.Schemas;
using PCStore.Schemas.DTO;
using PCStore.Schemas.Request;

namespace PCStore.Services
{
    class ProductService
    {
        private const string GetAllProductsUrl = "https://pcstore.space/v1/search/get_all_products";

        public async Task<List<BasketDTO>> GetAllProducts()
        {
            try
            {
                var request = new HttpRequestMessage(HttpMethod.Get, GetAllProductsUrl);
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





        public async Task<List<ProductItemModel>> ProductsList(List<BasketDTO> products)
        {
            try
            {
                var result = new List<ProductItemModel>();
                var productDictionary = new Dictionary<string, ProductItemModel>();

                foreach (var product in products)
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

                    ProcessProduct(product.Cpus, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Gpus, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Rams, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Motherboards, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.PuS, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Cases, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.HDDs, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.SSDs, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.M2SSds, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Vents, p => new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = $"https://pcstore.space/{p.Image}.jpg",
                        Counter = 1,
                        Article = p.Article
                    });

                    ProcessProduct(product.Coolers, p => new ProductItemModel
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
