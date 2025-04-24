using PCStore.Schemas;
using PCStore.Schemas.DTO;
using PCStore.Services;


namespace PCStore.Pages;

public partial class SpecsPage : ContentPage
{
    public ProductItemModel product;
	public SpecsPage(ProductItemModel _product)
	{
		InitializeComponent();
        product = _product;
        Initialize();
        
	}

    public async void Initialize()
    {
        var product_ = await SelectType(product.Article);
    }

    public async Task<object> SelectType(string article)
    {
        try
        {
            object product = null;

            switch (true)
            {
                case bool _ when article.Contains("CPU"):
                    product = await FindComponentsByArticles<CPU_DTO>(article);
                    break;

                case bool _ when article.Contains("GPU"):
                    product = await FindComponentsByArticles<GPU_DTO>(article);
                    break;

                case bool _ when article.Contains("RAM"):
                    product = await FindComponentsByArticles<RAM_DTO>(article);
                    break;

                case bool _ when article.Contains("MB"):
                    product = await FindComponentsByArticles<Motherboard_DTO>(article);
                    break;

                case bool _ when article.Contains("M2"):
                    product = await FindComponentsByArticles<M2_SSD_DTO>(article);
                    break;

                case bool _ when article.Contains("SSD"):
                    product = await FindComponentsByArticles<SSD_DTO>(article);
                    break;

                case bool _ when article.Contains("HDD"):
                    product = await FindComponentsByArticles<HDD_DTO>(article);
                    break;

                case bool _ when article.Contains("PU"):
                    product = await FindComponentsByArticles<POWER_UNIT_DTO>(article);
                    break;

                case bool _ when article.Contains("TOWER"):
                    product = await FindComponentsByArticles<Cooler_DTO>(article);
                    break;

                case bool _ when article.Contains("VENT"):
                    product = await FindComponentsByArticles<VENT_DTO>(article);
                    break;

                case bool _ when article.Contains("CASE"):
                    product = await FindComponentsByArticles<PC_Case_DTO>(article);
                    break;
            }

            return product;
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
            return null;
        }
        
    }

    public async Task<object> FindComponentsByArticles<T>(string article) where T : class
    {
        try
        {
            BasketService service = new BasketService();
            var list = await service.CheckBasket();
            foreach (var item in list)
            {
                var properties = item.GetType().GetProperties();

                foreach (var property in properties)
                {
                    var value = property.GetValue(item) as T;
                    if (value == null) continue;

                    var articleProperty = typeof(T).GetProperty("Article");
                    if (articleProperty == null) continue;

                    var componentArticle = articleProperty.GetValue(value) as string;
                    if (componentArticle == article)
                    {
                        return value;
                    }
                }
            }

            return null;
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
            return null;
        }
        
    }
}