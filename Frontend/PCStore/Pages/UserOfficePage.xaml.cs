using PCStore.Services;
using PCStore.Schemas;
using System.Threading.Tasks;
namespace PCStore.Pages;

public partial class UserOfficePage : ContentPage
{
	public UserOfficePage()
	{
		InitializeComponent();
        InitializeProfile();

    }


    private async void InitializeProfile()
    {
        await GetProfile();
    }

	private async Task GetProfile()
	{
		UserService userService = new UserService();
		AuthentificatedHttpClientService client = new AuthentificatedHttpClientService(new UserService());
		Task<UserSchema> userTask = userService.GetProfile(client);
		UserSchema user = await userTask;
		TitleLabel.Text = $"{user.Name} {user.Surname}";
		
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