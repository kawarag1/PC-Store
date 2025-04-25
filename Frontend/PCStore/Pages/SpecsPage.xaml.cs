using PCStore.Schemas;
using PCStore.Schemas.DTO;
using PCStore.Services;

namespace PCStore.Pages;

public partial class SpecsPage : ContentPage
{
    public ProductItemModel product_;
	public SpecsPage(ProductItemModel _product)
	{
		InitializeComponent();
        product_ = _product;
        Initialize();
        
	}

    public async void Initialize()
    {
        try
        {
            var (product, productType) = await SelectType(product_.Article);

            if (product != null && productType != null)
            {
                var listType = typeof(List<>).MakeGenericType(productType);
                var typedList = (System.Collections.IList)Activator.CreateInstance(listType);
                typedList.Add(product);

                ProductView.ItemsSource = typedList;
                LabelTitle.Text = $"Характеристики {product_.Name}";
            }
            else
            {
                ProductView.ItemsSource = null;
            }
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", $"Не удалось загрузить продукт: {ex.Message}", "OK");
        }


    }

    public async Task<(object Product, Type ProductType)> SelectType(string article)
    {
        try
        {
            var typeMappings = new Dictionary<string, Type>
            {
                ["CPU"] = typeof(CPU_DTO),
                ["GPU"] = typeof(GPU_DTO),
                ["RAM"] = typeof(RAM_DTO),
                ["MB"] = typeof(Motherboard_DTO),
                ["M2"] = typeof(M2_SSD_DTO),
                ["SSD"] = typeof(SSD_DTO),
                ["HDD"] = typeof(HDD_DTO),
                ["PU"] = typeof(POWER_UNIT_DTO),
                ["TOWER"] = typeof(Cooler_DTO),
                ["VENT"] = typeof(VENT_DTO),
                ["CASE"] = typeof(PC_Case_DTO)
            };

            foreach (var mapping in typeMappings)
            {
                if (article.StartsWith(mapping.Key))
                {
                    var product = await FindComponentsByArticles<ProductItemModel>(article, mapping.Value);
                    return (product, mapping.Value);
                }
            }

            return (null, null);
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
            return (null, null);
        }

    }

    public async Task<object> FindComponentsByArticles<T>(string article, Type targetType) where T : class
    {
        try
        {
            SearchService searchService = new SearchService();
            var productsDto = await searchService.GetAllProducts();

            if (productsDto == null)
                return null;

            var componentCollections = new List<IEnumerable<object>>
        {
            productsDto.Cpus,
            productsDto.Gpus,
            productsDto.Rams,
            productsDto.Motherboards,
            productsDto.PuS,
            productsDto.Cases,
            productsDto.HDDs,
            productsDto.SSDs,
            productsDto.M2SSds,
            productsDto.Vents,
            productsDto.Coolers
        };

            foreach (var collection in componentCollections)
            {
                if (collection == null) continue;

                foreach (var component in collection)
                {
                    if (!targetType.IsInstanceOfType(component))
                        continue;

                    var articleProperty = targetType.GetProperty("Article");
                    if (articleProperty == null)
                        continue;

                    var componentArticle = articleProperty.GetValue(component) as string;
                    if (componentArticle == article)
                    {
                        return component;
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