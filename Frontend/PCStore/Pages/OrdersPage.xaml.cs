using System.Threading.Tasks;
using PCStore.Schemas.DTO;
using PCStore.Services;

namespace PCStore.Pages;

public partial class OrdersPage : ContentPage
{

	public OrdersPage()
	{
		InitializeComponent();
		Initialize();

    }


	public async void Initialize()
	{
		OrderService service = new OrderService();
		var OrderList = await service.CheckOrder();
		OrdersCollection.ItemsSource = OrderList;
	}

    private async void OrdersCollection_SelectionChanged(object sender, SelectionChangedEventArgs e)
    {
		if (OrdersCollection.SelectedItem is OrderDTO order)
		{
			OrderService service = new OrderService();
			var orderList = new List<OrderDTO>();
			orderList.Add(order);
			var list = await service.OrderList(orderList);
            await Navigation.PushAsync(new SingleOrderPage(list, order.Id));
        }

		
    }
}