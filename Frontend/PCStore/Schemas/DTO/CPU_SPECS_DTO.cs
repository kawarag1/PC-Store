using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    class CPU_SPECS_DTO
    {
        [JsonProperty("frequency")]
        public double Frequency { get; set; }

        [JsonProperty("core_count")]
        public int Core_count { get; set; }

        [JsonProperty("cache")]
        public int Cache {  get; set; }

        [JsonProperty("tdp")]
        public int TDP { get; set; }

        [JsonProperty("flow_count")]
        public int Flow_count { get; set; }

        [JsonProperty("sockets")]
        public SocketDTO Sockets { get; set; }
    }
}
