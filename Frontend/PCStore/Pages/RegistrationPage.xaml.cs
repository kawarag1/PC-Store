using PCStore.Schemas;
using PCStore.Services;

namespace PCStore.Pages;

public partial class RegistrationPage : ContentPage
{
	public RegistrationPage()
	{
		InitializeComponent();
	}


    private async void RegBtn_Clicked(object sender, EventArgs e)
    {
        UserSchema user = new UserSchema();
        user.Login = LoginValue.Text;
        user.Password = PasswordValue.Text;
        user.Email = EmailValue.Text;


        HttpClient client = new HttpClient();
        UserService service = new UserService();

        bool isSuccess = await service.RegUser(user, client);

        if (isSuccess)
        {
            await Navigation.PushAsync(new UserOfficePage());

        }
    }

    private async void HaveAccBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PopAsync();
    }
}