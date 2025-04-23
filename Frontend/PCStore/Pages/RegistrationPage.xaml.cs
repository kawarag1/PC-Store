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
        try
        {
            UserSchema user = new UserSchema();
            user.login = LoginValue.Text;
            user.password = PasswordValue.Text;
            user.email = EmailValue.Text;


            HttpClient client = new HttpClient();
            UserService service = new UserService();

            bool isSuccess = await service.RegUser(user, client);

            if (isSuccess)
            {
                await Navigation.PushAsync(new UserOfficePage());

            }
        }
        catch (Exception ex)
        {
            await Shell.Current.DisplayAlert("Ошибка", "Непредвиденная ошибка, попробуйте указать другой логин", "OK");
        }
        
        
    }

    private async void HaveAccBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PopAsync();
    }
}