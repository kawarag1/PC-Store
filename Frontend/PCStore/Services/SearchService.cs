using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using PCStore.Schemas;
using PCStore.Schemas.DTO;

namespace PCStore.Services
{
    class SearchService
    {
        private const string GetAllProductsUrl = "https://pcstore.space/v1/search/get_all_products";

        public async Task<ProductsDTO> GetAllProducts()
        {
            try
            {
                HttpClient client = new HttpClient();
                var response = await client.GetAsync(GetAllProductsUrl);

                if (response.IsSuccessStatusCode)
                {
                    string responseJson = await response.Content.ReadAsStringAsync();
                    var products = JsonConvert.DeserializeObject<ProductsDTO>(responseJson);

                    return products;
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

        public async Task<List<ProductItemModel>> ConvertProducts(ProductsDTO products)
        {
            try
            {
                List<ProductItemModel> list = new List<ProductItemModel>();

                foreach (var p in products.Cpus)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Gpus)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Rams)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Motherboards)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.HDDs)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.SSDs)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.M2SSds)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Cases)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Vents)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.PuS)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                foreach (var p in products.Coolers)
                {
                    ProductItemModel model = new ProductItemModel
                    {
                        Id = p.Id,
                        Name = p.Name,
                        Cost = p.Cost,
                        ImageUrl = p.Image,
                        Counter = 1,
                        Article = p.Article
                    };
                    list.Add(model);
                }

                return list;
            }
            catch (Exception ex)
            {
                await Shell.Current.DisplayAlert("Ошибка", ex.Message, "OK");
                return null;
            }
        }
    }
}
