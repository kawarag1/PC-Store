using PCStore.Schemas;
using PCStore.Services;
using System.Threading.Tasks;

namespace PCStore.Pages;

public partial class SecondAuthPage : ContentPage
{
	public SecondAuthPage()
	{
		InitializeComponent();
        NavigationPage.SetHasNavigationBar(this, false);
        NavigationPage.SetHasBackButton(this, false);
		
    }

    private async void NonRegBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new RegistrationPage());
    }

    private async void AuthBtn_Clicked(object sender, EventArgs e)
    {

        string login = LoginValue.Text;
        string password = PasswordValue.Text;


        HttpClient client = new HttpClient();
        UserService service = new UserService();

        bool isSuccess = await service.Auth(login, password, client);

        if (isSuccess)
        {
            await Navigation.PushAsync(new UserOfficePage());

        }
    }
}