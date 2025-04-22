using PCStore.Services;
using PCStore.Schemas;
using System.Threading.Tasks;
namespace PCStore.Pages;

public partial class UserOfficePage : ContentPage
{
    private bool _isFirstLoad = false;
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

            if (string.IsNullOrEmpty(user.Name) || string.IsNullOrEmpty(user.Surname))
            {
                await Shell.Current.DisplayAlert("Предупреждение", "Перейдите в профиль для добавления личных  данных", "OK");
            }
            else
            {
                TitleLabel.Text = $"{user.Name} {user.Surname}";
            }
        }
        catch (Exception ex)
        {

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