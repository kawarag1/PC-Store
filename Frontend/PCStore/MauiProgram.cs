using Microsoft.Extensions.Logging;
using PCStore.Services;
using PCStore.Pages;
namespace PCStore
{
    public static class MauiProgram
    {
        public static IServiceProvider ServiceProvider { get; private set; }
        public static MauiApp CreateMauiApp()
        {
            var builder = MauiApp.CreateBuilder();
            builder
                .UseMauiApp<App>()
                .ConfigureFonts(fonts =>
                {
                    fonts.AddFont("OpenSans-Regular.ttf", "OpenSansRegular");
                    fonts.AddFont("OpenSans-Semibold.ttf", "OpenSansSemibold");
                });

#if DEBUG
    		builder.Logging.AddDebug();
            builder.Services.AddTransient<AuthentificatedHttpClientService>();
            builder.Services.AddTransient<AuthPage>();
            builder.Services.AddTransient<SecondAuthPage>();
            builder.Services.AddTransient<BasketPage>();
            builder.Services.AddTransient<ProfilePage>();
            builder.Services.AddTransient<RegistrationPage>();
            builder.Services.AddTransient<UserOfficePage>();
            builder.Services.AddSingleton<UserService>();
            
            builder.Services.AddSingleton<AuthentificatedHttpClientService>();
#endif

            var app = builder.Build();
            ServiceProvider = app.Services;
            return app;
        }
    }
}
