using PCStore.Services;
using PCStore.Schemas;
using System.Threading.Tasks;
namespace PCStore.Pages;

public partial class ProfilePage : ContentPage
{
	public ProfilePage()
	{
		InitializeComponent();
		GetProfile();

    }

	private async Task GetProfile()
	{
		UserService userService = new UserService();
		AuthHttpClientService client = new AuthHttpClientService(new UserService());
		Task<UserSchema> userTask = userService.GetProfile(client);
		UserSchema user = await userTask;
		Title = $"{user.Name} {user.Surname}";
		
	}


    private void ProfileBtn_Clicked(object sender, EventArgs e)
    {

    }

    private async Task PoliticBtn_Clicked(object sender, EventArgs e)
    {
        await DisplayAlert($"Политика конфиденциальности", "Подтвердите своё согласие, нажав по кнопке ОК", "ОК");
    }

    private void HelpBtn_Clicked(object sender, EventArgs e)
    {

    }

    private void OrderBtn_Clicked(object sender, EventArgs e)
    {

    }
}