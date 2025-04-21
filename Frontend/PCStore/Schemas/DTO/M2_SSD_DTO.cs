using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class M2_SSD_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("image")]
        public string Image { get; set; }

        [JsonProperty("article")]
        public string Article { get; set; }

        [JsonProperty("cost")]
        public double Cost { get; set; }

        [JsonProperty("specs")]
        public M2_SSD_SPECS_DTO Specs { get; set; }

        [JsonProperty("m2Size")]
        public M2_Size_DTO Size { get; set; }
    }
}
