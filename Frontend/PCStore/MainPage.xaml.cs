using PCStore.Schemas.DTO;
using PCStore.Schemas;
using PCStore.Pages;
using PCStore.Services;
using System.Collections.ObjectModel;

namespace PCStore
{
    public partial class MainPage : ContentPage
    {
        List<(string Name, string Model)> filters_ = new List<(string Name, string Model)>();
        private ObservableCollection<ProductItemModel> ProductItems;
        public MainPage()
        {
            InitializeComponent();
            CollectionInitialize();
            FiltersInitialize();
        }

        private void FiltersInitialize()
        {
            var filters = new List<(string Name, string Model)>
            {
                ("Без фильтра", null),
                ("Процессор", "CPU"),
                ("Видеокарта", "GPU"),
                ("Оперативная память", "RAM"),
                ("Кулер", "TOWER"),
                ("Блок питания", "PU"),
                ("Корпус", "CASE"),
                ("Жёсткий диск", "HDD"),
                ("Твердотельный накопитель", "SSD"),
                ("М2 накопитель", "M2"),
                ("Материнская плата", "MB"),
                ("Вентилятор", "VENT")
            };
            FilterPricker.ItemsSource = filters.Select(x => x.Name).ToList();
            filters_ = filters;
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
                string selectedFilter = picker.Items[index].ToString();
                var model_ = filters_.Where(x => x.Name == selectedFilter).FirstOrDefault();
                if (selectedFilter == "Без фильтра")
                {
                    ProductsInSearch.ItemsSource = ProductItems;
                }
                else
                {
                    List<ProductItemModel> products = ProductItems.Where(x => x.Article.Contains(model_.Model)).ToList();
                    ProductsInSearch.ItemsSource = products;
                }
                   
            }
        }

        private void Search_Clicked(object sender, EventArgs e)
        {
            if(QueryForSearching.Text != null)
            {
                List<ProductItemModel> products = ProductItems.Where(x => x.Name.Contains(QueryForSearching.Text)).ToList();
                ProductsInSearch.ItemsSource = products;
            }   
            else
            {
                ProductsInSearch.ItemsSource = ProductItems;
            }
            

        }
    }

}
