using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class RAM_SPECS_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("frequency")]
        public int Frequency { get; set; }

        [JsonProperty("radiators")]
        public bool Radiators { get; set; }

        [JsonProperty("ram_quantities")]
        public RAM_Quantities_DTO RAM_Quantities { get; set; }

        [JsonProperty("types")]
        public RAM_Types_DTO RAM_Types { get; set; }
    }
}
