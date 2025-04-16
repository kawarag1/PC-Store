using PCStore.Schemas;
using PCStore.Services;

namespace PCStore.Pages;

public partial class SecondAuthPage : ContentPage
{
	public SecondAuthPage()
	{
		InitializeComponent();
        NavigationPage.SetHasNavigationBar(this, false);
        NavigationPage.SetHasBackButton(this, false);
		
    }

    private void NonRegBtn_Clicked(object sender, EventArgs e)
    {

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
            Navigation.PushAsync(new UserOfficePage());

        }
    }
}