using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Newtonsoft.Json;

namespace PCStore.Schemas.DTO
{
    public class Cooler_Sockets_DTO
    {
        [JsonProperty("id")]
        public int Id { get; set; }

        [JsonProperty("socket_id")]
        public int Socket_Id { get; set; }

        [JsonProperty("cooler_id")]
        public int Cooler_id { get; set; }

        [JsonProperty("sockets")]
        public SocketDTO Sockets { get; set; }
    }
}
