using PCStore.Services;
using PCStore.Schemas;
using System.Threading.Tasks;
namespace PCStore.Pages;

public partial class UserOfficePage : ContentPage
{
    UserSchema _user;
	public UserOfficePage()
	{
		InitializeComponent();
        

    }


    protected override async void OnAppearing()
    {
        base.OnAppearing();
        InitializeProfile();
    }

    private async void InitializeProfile()
    {
        await GetProfile();
    }

    private async Task GetProfile()
	{
        try
        {
            UserService userService = new UserService();
            Task<UserSchema> userTask = userService.GetProfile();
            UserSchema user = await userTask;

            if (user == null)
            {
                await Shell.Current.DisplayAlert("Ошибка", "Не удалось получить данные, пожалуйста, авторизуйтесь снова", "OK");
                return;
            }
            _user = user;
            if (string.IsNullOrEmpty(user.name) || string.IsNullOrEmpty(user.surname))
            {
                await Shell.Current.DisplayAlert("Предупреждение", "Перейдите в профиль для добавления личных  данных", "OK");
            }
            else
            {
                TitleLabel.Text = $"{user.name} {user.surname}";
            }
        }
        catch (Exception ex)
        {

        }
		
        
	}


    private async void ProfileBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new ProfilePage(_user));
    }

    private async void PoliticBtn_Clicked(object sender, EventArgs e)
    {
        await DisplayAlert($"Политика конфиденциальности", "Подтвердите своё согласие, нажав по кнопке ОК", "ОК");
    }

    private void HelpBtn_Clicked(object sender, EventArgs e)
    {

    }

    private async void OrderBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new OrdersPage());
    }

    protected override bool OnBackButtonPressed()
    {
        
        return true;
    }
}