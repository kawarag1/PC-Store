using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;
using Newtonsoft.Json.Converters;

namespace PCStore.Schemas
{
    public class UserSchema
    {
        [JsonProperty("login")]
        public string login { get; set; }

        [JsonProperty("password")]
        public string password { get; set; }

        [JsonProperty("email")]
        public string email { get; set; }

        [JsonProperty("name")]
        public string? name { get; set; }

        [JsonProperty("surname")]
        public string? surname { get; set; }

        [JsonProperty("patronymic")]
        public string? patronymic { get; set; }


    }

}
