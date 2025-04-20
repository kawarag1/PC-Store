using PCStore.Services;
using PCStore.Schemas;
using System.Threading.Tasks;
namespace PCStore.Pages;

public partial class UserOfficePage : ContentPage
{
    private bool _isFirstLoad = true;
	public UserOfficePage()
	{
		InitializeComponent();
        OnAppearing();

    }


    protected override async void OnAppearing()
    {
        base.OnAppearing();
        if (_isFirstLoad)
        {
            await GetProfile();
            _isFirstLoad = false;
        }
        
    }

    private async Task GetProfile()
	{
		UserService userService = new UserService();
		AuthentificatedHttpClientService client = new AuthentificatedHttpClientService(new UserService());
		Task<UserSchema> userTask = userService.GetProfile(client);
		UserSchema user = await userTask;
        if (user.Name == null || user.Surname == null)
        {
            await Shell.Current.DisplayAlert("Предупреждение", "Перейдите в профиль для добавления личных  данных", "OK");
        }
        else
        {
            TitleLabel.Text = $"{user.Name} {user.Surname}";
        }
	}


    private async void ProfileBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new ProfilePage());
    }

    private async void PoliticBtn_Clicked(object sender, EventArgs e)
    {
        await DisplayAlert($"Политика конфиденциальности", "Подтвердите своё согласие, нажав по кнопке ОК", "ОК");
    }

    private void HelpBtn_Clicked(object sender, EventArgs e)
    {

    }

    private void OrderBtn_Clicked(object sender, EventArgs e)
    {

    }

    protected override bool OnBackButtonPressed()
    {
        
        return true;
    }
}