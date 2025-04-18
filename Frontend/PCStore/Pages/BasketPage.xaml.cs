using PCStore.Services;
using System.Collections.ObjectModel;
using Windows.Media.Protection.PlayReady;

namespace PCStore.Pages;

public partial class BasketPage : ContentPage
{
    //ObservableCollection<Product> _products = new ObservableCollection<Product>();
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

    private void SelectProductBox_CheckedChanged(object sender, CheckedChangedEventArgs e)
    {
        //try
        //{
        //    var checkbox = (CheckBox)sender;
        //    if (checkbox.BindingContext is Product product)
        //    {
        //        if (checkbox.IsChecked == true)
        //        {
        //            _products.Add(product);
        //        }
        //        else
        //        {
        //            _products.Remove(product);
        //        }
        //    }
        //}
        //catch (Exception ex)
        //{

        //}
    }
}