using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class PC_Case_SPECS_DTO
    {
        [JsonProperty("id")]
        public string Id { get; set; }

        [JsonProperty("length")]
        public int Length { get; set; }

        [JsonProperty("height")]
        public int Height { get; set; }

        [JsonProperty("wigth")]
        public int Width { get; set; }

        [JsonProperty("rear_vents_count")]
        public int Rear_vents_count { get; set; }

        [JsonProperty("front_vents_count")]
        public int Front_vents_count { get; set; }

        [JsonProperty("types")]
        public Case_Type_DTO Case_Type { get; set; }

        [JsonProperty("sizes")]
        public VENT_Size_DTO Vent_Size { get; set; }

        
    }
}
