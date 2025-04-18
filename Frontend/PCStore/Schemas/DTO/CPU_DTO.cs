using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    class CPU_DTO
    {
        [JsonProperty]
        public int id { get; set; }

        [JsonProperty]
        public int cost { get; set; }

        [JsonProperty]
        public string image { get; set; }

        [JsonProperty]
        public string name { get; set; }

        [JsonProperty]
        public string article { get; set; }

        [JsonProperty]
        public Manufacturers_DTO manufacturers { get; set; }

        [JsonProperty]
        public CPU_SPECS_DTO specs { get; set; }
    }
}
