using PCStore.Services;

namespace PCStore.Pages;

public partial class BasketPage : ContentPage
{
	public BasketPage()
	{
		InitializeComponent();
        CollectionInitialize();
	}

    private void CollectionInitialize()
    {

        if (UserService.IsAuth())
        {
            if (ProductsInBasket.ItemsSource == null)
            {
                Hat.IsVisible = false;
                Basement.IsVisible = false;
            }
            
        }
        else
        {
            Hat.IsVisible = false;
            Basement.IsVisible = false;
            LabelIfEmpty.Text = "Для добавления товаров в корзину требуется пройти авторизацию";
            NonAuthIcon.IsVisible = true;
        }
    }

    private void SelectingAllBox_CheckedChanged(object sender, CheckedChangedEventArgs e)
    {

    }

    

    private void Button_Clicked(object sender, EventArgs e)
    {

    }

    private void PlusCounter(object sender, TappedEventArgs e)
    {

    }

    private void MinusCounter(object sender, TappedEventArgs e)
    {

    }

    private void TapGestureRecognizer_Tapped(object sender, TappedEventArgs e)
    {

    }
}