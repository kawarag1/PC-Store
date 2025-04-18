﻿using System.Threading.Tasks;
using PCStore.Pages;
using PCStore.Services;

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
            bool isauth = UserService.IsAuth();
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
            string login = await SecureStorage.GetAsync("login");
            string password = await SecureStorage.GetAsync("password");

            HttpClient client = new HttpClient();
            UserService service = new UserService();

            bool isSuccess = await service.Auth(login, password, client);
            return isSuccess;

        }


        private async Task ForceUpdateContent(Page newPage)
        {
            var tempContent = new ShellContent
            {
                ContentTemplate = new DataTemplate(() => newPage)
            };

            DinamicContent.ContentTemplate = tempContent.ContentTemplate;

            await Task.Delay(50);
        }


        private async Task ClearStorage()
        {
            try
            {
                bool loginRemove = SecureStorage.Remove("login");
                bool passwordRemove = SecureStorage.Remove("password");
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
