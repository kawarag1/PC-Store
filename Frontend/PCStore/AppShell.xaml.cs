using System.Threading.Tasks;
using PCStore.Pages;
using PCStore.Services;
using Microsoft.Extensions.DependencyInjection;

namespace PCStore
{   
    public partial class AppShell : Shell
    {
        private bool _isUpdating = true;
        public AppShell()
        {
            InitializeComponent();
            InitializeDynamicContent();
            

        }

        private async void InitializeDynamicContent()
        {
            bool isauth = await AuthUser();
            await UpdateContent(isauth);
        }

        private async Task UpdateContent(bool isAuth)
        {
            if (isAuth)
            {

                await MainThread.InvokeOnMainThreadAsync(async () =>
                {
                    bool isSuccess = await AuthUser();
                    if (isSuccess)
                    {
                        await ForceUpdateContent(new UserOfficePage());
                        
                    }
                    else
                    {
                        await ClearStorage();
                        await DisplayAlert("Ошибка", "Неверный логин или пароль", "OK");
                        await ForceUpdateContent(new AuthPage());
                    }
                });
            }
            else
            {   
                await ForceUpdateContent(new AuthPage());
            }
            
        }

        private async Task<bool> AuthUser()
        {
            string token = await SecureStorage.GetAsync("acess_token");
            if (token == null)
            {
                return false;
            }
            else
            {
                return true;
            }
        }

        private async Task ForceUpdateContent(Page newPage)
        {
            var tempContent = new ShellContent
            {
                ContentTemplate = new DataTemplate(() => newPage)
            };

                DynamicContent.ContentTemplate = tempContent.ContentTemplate;
                NavBar.IsEnabled = false;

                await Task.Delay(50);
        }


        private async Task ClearStorage()
        {
            try
            {
                bool accessRemove = SecureStorage.Remove("access_token");
                bool refreshRemove = SecureStorage.Remove("refresh_token");
            }
            catch (Exception ex)
            {
                await DisplayAlert("Ошибка", "Не удалось очистить сохраненные данные", "OK");
            }
            
        }

    }
}
