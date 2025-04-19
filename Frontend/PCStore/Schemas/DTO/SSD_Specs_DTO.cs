using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    internal class SSD_Specs_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("tdp")]
        public int TDP { get; set; }

        [JsonProperty("speed_read")]
        public int Speed_read { get; set; }

        [JsonProperty("write_read")]
        public int Speed_write { get; set; }

        [JsonProperty("memories")]
        public MemorySize_DTO Memories { get; set; }
    }
}
