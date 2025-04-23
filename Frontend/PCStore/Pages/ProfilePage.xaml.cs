using PCStore.Schemas;
using PCStore.Services;

namespace PCStore.Pages;

public partial class ProfilePage : ContentPage
{
	public ProfilePage(UserSchema user)
	{
		InitializeComponent();
        Initialize(user);

    }


	private async void Initialize(UserSchema user)
	{
        if (string.IsNullOrEmpty(user.name) || string.IsNullOrEmpty(user.surname) || string.IsNullOrEmpty(user.patronymic))
        {
            LoginValue.Text = user.login;
            PasswordValue.Text = await SecureStorage.GetAsync("password");
            EmailValue.Text = user.email;
            NameValue.Text = "";
            SurnameValue.Text = "";
            PatronymicValue.Text = "";
        }
        else
        {
            LoginValue.Text = user.login;
            PasswordValue.Text = await SecureStorage.GetAsync("password");
            EmailValue.Text = user.email;
            NameValue.Text = user.name;
            SurnameValue.Text = user.surname;
            PatronymicValue.Text = user.patronymic;
        }
    }

    private async void SaveBtn_Clicked(object sender, EventArgs e)
    {
        UserSchema userSchema = new UserSchema();
        userSchema.name = NameValue.Text;
        userSchema.surname = SurnameValue.Text;
        userSchema.patronymic = PatronymicValue.Text;
        userSchema.login = LoginValue.Text;
        userSchema.password = PasswordValue.Text;
        userSchema.email = EmailValue.Text;
        UserService service = new UserService();
        bool result = await service.UpdateProfile(userSchema);
        if (result)
        { 
            await DisplayAlert("Успешно", "Данные успешно обновлены!", "OK");
            await SecureStorage.SetAsync("login", LoginValue.Text);
            await SecureStorage.SetAsync("password", PasswordValue.Text);
            Initialize(userSchema);
        }
        else
        {
            await DisplayAlert("Ошибка", "Произошла непредвиденная ошибка, возможно этот логин занят", "OK");
        }
    }

    private void TapGestureRecognizer_Tapped(object sender, TappedEventArgs e)
    {
        if (PasswordValue.IsPassword == true)
        {
            PasswordValue.IsPassword = false;
        }
        else
        {
            PasswordValue.IsPassword = true;
        }
    }

    private async void TapGestureRecognizer_Tapped_1(object sender, TappedEventArgs e)
    {
        var keys = new List<string> { "login", "password", "access_token", "refresh_token" };
        foreach (var key in keys)
        {
            SecureStorage.Remove(key);
        }

        await Navigation.PushAsync(new AuthPage());
    }
}