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
        [JsonProperty]
        public double frequency { get; set; }

        [JsonProperty]
        public int core_count { get; set; }

        [JsonProperty]
        public int cache {  get; set; }

        [JsonProperty]
        public int tdp { get; set; }

        [JsonProperty]
        public int flow_count { get; set; }

        [JsonProperty]
        public SocketDTO sockets { get; set; }
    }
}
