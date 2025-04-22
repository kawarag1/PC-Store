using System.Threading.Tasks;
using PCStore.Pages;
using PCStore.Services;
using Microsoft.Extensions.DependencyInjection;

namespace PCStore
{   
    public partial class AppShell : Shell
    {
        public AppShell()
        {
            InitializeComponent();
            InitializeDynamicContent();
            

        }

        private async void InitializeDynamicContent()
        {
            await UpdateContent();
        }

        private async Task UpdateContent()
        {
            await MainThread.InvokeOnMainThreadAsync(async () =>
            {
                bool isSuccess = await AuthUser();
                if (isSuccess == true)
                {
                    await ForceUpdateContent(new UserOfficePage());

                }
                else
                {
                    await ForceUpdateContent(new AuthPage());
                }
            });
        }

        private async Task<bool> AuthUser()
        {
            string token = await SecureStorage.GetAsync("access_token");

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
    }
}
