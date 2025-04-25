using Microsoft.Maui.Controls.Internals;
using PCStore.Schemas;
using PCStore.Schemas.Request;
using PCStore.Services;
using System.Collections.ObjectModel;
using System.Threading.Tasks;

namespace PCStore.Pages;

public partial class BasketPage : ContentPage
{
    private double TotalPrice;
    private int ProductCounter;
    private ObservableCollection<ProductItemModel> ProductItems;
    private List<ProductItemModel> ProductList = new List<ProductItemModel>();
    private int SoloProductCounter;
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
                ProductsSum.Text = $"{TotalPrice} ₽";
                ProductsCounter.Text = $"{ProductCounter}";
                ObservableCollection<ProductItemModel> productsList = new ObservableCollection<ProductItemModel>(products);
                ProductItems = productsList;
                ProductsInBasket.ItemsSource = ProductItems;
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
        //var itemcopy = ProductItems.ToList();
        foreach (var item in ProductItems)
        {
            item.IsSelected = true;
        }

        //var newCollection = new ObservableCollection<ProductItemModel>(itemcopy);
        //ProductsInBasket.ItemsSource = null;
        //ProductsInBasket.ItemsSource = newCollection;
        //SelectAllItems(e.Value);
        //ProductItems.Where(x => !x.IsSelected).ToList().ForEach(x => x.IsSelected = true);

    }

    private void SelectAllItems(bool isSelected)
    {
        foreach (var item in ProductItems)
        {
            item.IsSelected = isSelected;
        }

    }

    private async void Button_Clicked(object sender, EventArgs e)
    {
        try
        {
            if (ProductList == null)
            {
                await DisplayAlert("Ошибка", "Выберите товары, которые вы хотите заказать", "OK");
            }
            else
            {
                OrderService service = new OrderService();
                await service.CreateOrder(ProductList);
                await DisplayAlert("Уведомление", $"Заказ на сумму {TotalPrice}, создан", "OK");
                CollectionInitialize();
                TotalPrice = 0;
                ProductCounter = 0;
            }
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
        }
        
    }

    private async void TapGestureRecognizer_Tapped(object sender, TappedEventArgs e)
    {
        if (ProductList == null)
        {
            await DisplayAlert("Уведомление", "Выберите товары, которые вы хотите удалить из корзины", "OK");
        }
        else
        {
            BasketService service = new BasketService();
            await service.DeleteOneFromBasket(ProductList);
            CollectionInitialize();
            TotalPrice = 0;
            ProductCounter = 0;
        }
            
    }

    private async void SelectProductBox_CheckedChanged(object sender, CheckedChangedEventArgs e)
    {
        try
        {
            var checkbox = (CheckBox)sender;
            if (checkbox.BindingContext is ProductItemModel product)
            {
                if (checkbox.IsChecked == true)
                {
                    ProductList.Add(product);
                    TotalPrice += product.Cost * product.Counter;
                    ProductsSum.Text = $"{TotalPrice} ₽";
                    ProductCounter += product.Counter;
                    ProductsCounter.Text = ProductsCounter.Text = GetProductCountText(ProductCounter);
                }
                else
                {
                    ProductList.Remove(product);
                    if (TotalPrice == 0 || ProductCounter == 0)
                    {
                        return;
                    }
                    else
                    {
                        TotalPrice -= product.Cost * product.Counter;
                        ProductsSum.Text = $"{TotalPrice} ₽";
                        ProductCounter -= product.Counter;
                        ProductsCounter.Text = GetProductCountText(ProductCounter);
                    }
                        
                }
            }
        }
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
        }
    }

    private string GetProductCountText(int productCount)
    {
        int lastDigit = productCount % 10;
        int lastTwoDigits = productCount % 100;

        if (lastTwoDigits >= 11 && lastTwoDigits <= 14)
        {
            return $"{productCount} товаров";
        }

        switch (lastDigit)
        {
            case 1:
                return $"{productCount} товар";
            case 2:
            case 3:
            case 4:
                return $"{productCount} товара";
            default:
                return $"{productCount} товаров";
        }
    }

    private async void OnImageTapped(object sender, TappedEventArgs e)
    {
        try
        {
            var image = (Image)sender;
            if (image.BindingContext is ProductItemModel product)
            {
                await Navigation.PushAsync(new ProductPageFromBasket(product));
            }
        } 
        catch (Exception ex)
        {
            await DisplayAlert("Ошибка", ex.Message, "OK");
        }
    }

    private async void MinusCounter_Clicked(object sender, EventArgs e)
    {
        var button = (Button)sender;
        if (button.BindingContext is ProductItemModel product)
        {
            if (product.Counter == 1)
            {
                bool answer = await DisplayAlert("Предупреждение", "Вы хотите удалить этот товар из корзины?", "Да", "Нет");
                if (answer)
                {
                    BasketService service = new BasketService();
                    BasketRequest request = new BasketRequest();
                    request.id = product.Id;
                    request.article = product.Article;
                    service.DeleteOneFromBasket(request);
                    ProductItems.Remove(product);
                }
                else
                {
                    return;
                }
            }
            else
            {
                product.Counter--;
                var index = ProductItems.IndexOf(product);
                ProductItems.RemoveAt(index);
                ProductItems.Insert(index, product);
                TotalPrice = 0;
                ProductCounter = 0;
            }
        }
    }

    private void PlusCounter_Clicked(object sender, EventArgs e)
    {
        var button = (Button)sender;
        if (button.BindingContext is ProductItemModel product)
        {
            product.Counter++;
            var index = ProductItems.IndexOf(product);
            ProductItems.RemoveAt(index);
            ProductItems.Insert(index, product);
            TotalPrice = 0;
            ProductCounter = 0;
        }
    }
}