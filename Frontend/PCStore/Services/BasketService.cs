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

                foreach (var basket in  baskets)
                {
                    if (basket.Cpus != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Cpus.Id,
                            Name = basket.Cpus.Name,
                            Cost = basket.Cpus.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Cpus.Image}.jpg",
                            Counter = 1,
                            Article = basket.Cpus.Article
                        });
                    }

                    if (basket.Gpus != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Gpus.Id,
                            Name = basket.Gpus.Name,
                            Cost = basket.Gpus.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Gpus.Image}.jpg",
                            Counter = 1,
                            Article = basket.Gpus.Article
                        });
                    }

                    if (basket.Rams != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Rams.Id,
                            Name = basket.Rams.Name,
                            Cost = basket.Rams.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Rams.Image}.jpg",
                            Counter = 1,
                            Article = basket.Rams.Article
                        });
                    }

                    if (basket.Motherboards != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Motherboards.Id,
                            Name = basket.Motherboards.Name,
                            Cost = basket.Motherboards.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Motherboards.Image}.jpg",
                            Counter = 1,
                            Article = basket.Motherboards.Article
                        });
                    }

                    if (basket.PuS != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.PuS.Id,
                            Name = basket.PuS.Name,
                            Cost = basket.PuS.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.PuS.Image}.jpg",
                            Counter = 1,
                            Article = basket.PuS.Article
                        });
                    }

                    if (basket.Cases != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Cases.Id,
                            Name = basket.Cases.Name,
                            Cost = basket.Cases.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Cases.Image}.jpg",
                            Counter = 1,
                            Article = basket.Cases.Article
                        });
                    }

                    if (basket.HDDs != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.HDDs.Id,
                            Name = basket.HDDs.Name,
                            Cost = basket.HDDs.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.HDDs.Image}.jpg",
                            Counter = 1,
                            Article = basket.HDDs.Article
                        });
                    }

                    if (basket.SSDs != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.SSDs.Id,
                            Name = basket.SSDs.Name,
                            Cost = basket.SSDs.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.SSDs.Image}.jpg",
                            Counter = 1,
                            Article = basket.SSDs.Article
                        });
                    }

                    if (basket.M2SSds != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.M2SSds.Id,
                            Name = basket.M2SSds.Name,
                            Cost = basket.M2SSds.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.M2SSds.Image}.jpg",
                            Counter = 1,
                            Article = basket.M2SSds.Article
                        });
                    }

                    if (basket.Vents != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Vents.Id,
                            Name = basket.Vents.Name,
                            Cost = basket.Vents.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Vents.Image}.jpg",
                            Counter = 1,
                            Article = basket.Vents.Article
                        });
                    }

                    if (basket.Coolers != null)
                    {
                        result.Add(new ProductItemModel
                        {
                            Id = basket.Coolers.Id,
                            Name = basket.Coolers.Name,
                            Cost = basket.Coolers.Cost,
                            ImageUrl = $"https://pcstore.space/{basket.Coolers.Image}.jpg",
                            Counter = 1,
                            Article = basket.Coolers.Article
                        });
                    }
                }
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
