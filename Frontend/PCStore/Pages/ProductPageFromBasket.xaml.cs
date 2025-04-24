using PCStore.Schemas;

namespace PCStore.Pages;

public partial class ProductPageFromBasket : ContentPage
{
    public ProductItemModel product;
    public ProductPageFromBasket(ProductItemModel _product)
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
}