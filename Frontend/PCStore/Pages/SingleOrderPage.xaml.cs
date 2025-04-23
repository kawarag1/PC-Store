using System.Collections.ObjectModel;
using PCStore.Schemas;

namespace PCStore.Pages;

public partial class SingleOrderPage : ContentPage
{
    private ObservableCollection<ProductItemModel> ProductItems;
    public SingleOrderPage(List<ProductItemModel> list, int number)
	{
		InitializeComponent();
        Title.Text = $"Заказ №{number}";
        Initialize(list);
		

    }

	public async void Initialize(List<ProductItemModel> _list)
	{
		ProductItems = new ObservableCollection<ProductItemModel>(_list);
		ProductsInBasket.ItemsSource = ProductItems;
	}
}