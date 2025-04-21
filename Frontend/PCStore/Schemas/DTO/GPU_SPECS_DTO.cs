using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class GPU_SPECS_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("RTX_Rays")]
        public bool RTX_Rays { get; set; }

        [JsonProperty("amount_video_memory")]
        public int Amount_Video_Memory { get; set; }

        [JsonProperty("frequency")]
        public int Frequency { get; set; }

        [JsonProperty("tdp")]
        public int TDP { get; set; }

        [JsonProperty("GPU_Memory_Types")]
        public GPU_Memory_Types_DTO GPU_Memory_Types { get; set; }

        

    }
}
