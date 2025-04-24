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
        await Navigation.PushModalAsync(new SpecsPage(product));
    }
}