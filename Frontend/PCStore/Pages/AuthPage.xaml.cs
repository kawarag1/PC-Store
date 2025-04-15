using System.Threading.Tasks;

namespace PCStore.Pages;

public partial class AuthPage : ContentPage
{
	public AuthPage()
	{
		InitializeComponent();
        
	}

    private async void AuthBtn_Clicked(object sender, EventArgs e)
    {
        await Navigation.PushAsync(new SecondAuthPage());
    }

    private async void PoliticBnt_Clicked(object sender, EventArgs e)
    {
        await DisplayAlert($"�������� ������������������", "����������� ��� ��������, ����� �� ������ ��", "��");
    }

    protected override bool OnBackButtonPressed()
    {
        return true;
    }
}