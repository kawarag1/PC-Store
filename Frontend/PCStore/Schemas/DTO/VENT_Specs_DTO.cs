using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class VENT_Specs_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("max_level_noise")]
        public double Level_Noise { get; set; }

        [JsonProperty("min_speed_rotation")]
        public int MinSpeedRotation { get; set; }

        [JsonProperty("max_speed_rotation")]
        public int MaxSpeedRotation { get; set; }
    }
}
