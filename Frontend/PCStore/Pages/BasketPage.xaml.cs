using PCStore.Schemas;
using PCStore.Services;
using System.Collections.ObjectModel;
using System.Threading.Tasks;

namespace PCStore.Pages;

public partial class BasketPage : ContentPage
{
    private double TotalPrice;
    private int ProductCounter;
	public BasketPage()
	{
		InitializeComponent();
	}

    protected override void OnAppearing()
    {
        base.OnAppearing();
        CollectionInitialize();
    }

    private async Task CollectionInitialize()
    {
        var isauth = await UserService.IsAuth();

        if (isauth)
        {
            BasketService basketService = new BasketService();
            
            var _products = await basketService.CheckBasket();
            var products = await basketService.BasketList(_products);
            if (products == null)
            {
                Hat.IsVisible = false;
                Basement.IsVisible = false;
                NonAuthIcon.IsVisible = false;
            }
            else
            {
                
                ProductsInBasket.ItemsSource = products;
                foreach (var product in _products)
                {
                    try
                    {
                        TotalPrice += product.Cpus.Cost;
                        TotalPrice += product.Gpus.Cost;
                        TotalPrice += product.Rams.Cost;
                        TotalPrice += product.Motherboards.Cost;
                        TotalPrice += product.SSDs.Cost;
                        TotalPrice += product.HDDs.Cost;
                        TotalPrice += product.M2SSds.Cost;
                        TotalPrice += product.PuS.Cost;
                        TotalPrice += product.Cases.Cost;
                        TotalPrice += product.Vents.Cost;
                        TotalPrice += product.Coolers.Cost;
                    }
                    catch (Exception ex)
                    {
                        TotalPrice += 0;
                        continue;
                    }
                    
                    
                }
                ProductConter.Text = $"{_products.Count.ToString()} товар";
                ProductsSum.Text = $"{TotalPrice.ToString()} ₽";
                
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