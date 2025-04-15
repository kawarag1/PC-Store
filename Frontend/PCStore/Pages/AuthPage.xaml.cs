using System.Threading.Tasks;

namespace PCStore.Pages;

public partial class AuthPage : ContentPage
{
	public AuthPage()
	{
		InitializeComponent();
        
	}

    private async void AuthBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new SecondAuthPage());
    }

    private async Task PoliticBnt_Clicked(object sender, EventArgs e)
    {
        await DisplayAlert($"Политика конфиденциальности", "Подтвердите своё согласие, нажав по кнопке ОК", "ОК");
        
    }
}