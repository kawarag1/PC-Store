using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class Cooler_Specs_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("min_frequency")]
        public int MinFrequency { get; set; }

        [JsonProperty("max_frequency")]
        public int MaxFrequency { get; set; }

        [JsonProperty("dispassion")]
        public int Dispassion {  get; set; }

        [JsonProperty("radiator_material")]
        public Radiator_Material_DTO Radiator_Material { get; set; }

        [JsonProperty("base_material")]
        public Base_Material_DTO Base_Material { get; set; }
    }
}
