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
            FiltersInitialize();
        }

        private void FiltersInitialize()
        {
            List<string> filters = new List<string>
            {
                "Без фильтра",
                "Процессор",
                "Видеокарта",
                "Оперативная память",
                "Кулер",
                "Блок питания",
                "Корпус",
                "Жёсткий диск",
                "Твердотельный накопитель",
                "М2 накопитель",
                "Материнская плата",
                "Вентилятор"
            };
            FilterPricker.ItemsSource = filters;
            FilterPricker.SelectedIndex = 0;
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

        private void FilterPricker_SelectedIndexChanged(object sender, EventArgs e)
        {
            var picker = (Picker)sender;
            int index = picker.SelectedIndex;

            if (index != -1)
            {
                string slectedFilter = picker.Items[index].ToString();

            }
        }

        private void Search_Clicked(object sender, EventArgs e)
        {

        }
    }

}
