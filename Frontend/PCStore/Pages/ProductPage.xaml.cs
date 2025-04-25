using System.Threading.Tasks;
using PCStore.Schemas;
using PCStore.Services;

namespace PCStore.Pages;

public partial class ProductPage : ContentPage
{
    ProductItemModel product;
	public ProductPage(ProductItemModel _product)
	{
		InitializeComponent();
        product = _product;
        BindingContext = new { ProductItemModel = _product };

    }

    private async void SpecsBtn_Clicked(object sender, EventArgs e)
    {
        var _product = product;
        await Navigation.PushAsync(new SpecsPage(_product));
    }

    private async void AddToCartBtn_Clicked(object sender, EventArgs e)
    {
        BasketService basketService = new BasketService();
        List<ProductItemModel> products = new List<ProductItemModel>();
        products.Add(product);
        await basketService.AddToBasket(products);
        await DisplayAlert("Успешно!", "Товар добавлен в корзину!" ,"OK");
    }
}