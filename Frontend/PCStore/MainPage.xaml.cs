using PCStore.Schemas.DTO;
using PCStore.Schemas;
using PCStore.Pages;
using PCStore.Services;
using System.Collections.ObjectModel;

namespace PCStore
{
    public partial class MainPage : ContentPage
    {
        private ObservableCollection<ProductItemModel> ProductItems;
        public MainPage()
        {
            InitializeComponent();
            CollectionInitialize();
        }



        private async void CollectionInitialize()
        {
            try
            {
                SearchService SearchService = new SearchService();
                

                var _products = await SearchService.GetAllProducts();
                var products = await SearchService.ConvertProducts(_products);
                ObservableCollection<ProductItemModel> productsList = new ObservableCollection<ProductItemModel>(products);
                ProductItems = productsList;
                ProductsInSearch.ItemsSource = ProductItems;
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", ex.Message, "OK");
            }
            
        }

        private async void ProductsInSearch_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            try
            {
                ProductItemModel product = (ProductItemModel)ProductsInSearch.SelectedItem;
                await Navigation.PushAsync(new ProductPage(product));
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", ex.Message, "OK");
            }
        }
    }

}
