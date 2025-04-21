using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class CPU_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("cost")]
        public double Cost { get; set; }

        [JsonProperty("image")]
        public string Image { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("article")]
        public string Article { get; set; }

        [JsonProperty("manufacturers")]
        public Manufacturers_DTO Manufacturers { get; set; }

        [JsonProperty("specs")]
        public CPU_SPECS_DTO Specs { get; set; }
    }
}
