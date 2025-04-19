using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class POWER_UNIT_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("power")]
        public int Power {  get; set; }

        [JsonProperty("modular")]
        public bool Modular { get; set; }

        [JsonProperty("name")]
        public string Name { get; set; }

        [JsonProperty("article")]
        public string Article { get; set; }

        [JsonProperty("image")]
        public string Image { get; set; }

        [JsonProperty("cost")]
        public int Cost { get; set; }

        [JsonProperty("certs")]
        public Certificates_DTO Certificates { get; set; }

        [JsonProperty("manufacturers")]
        public Manufacturers_DTO Manufacturers { get; set; }
    }
}
