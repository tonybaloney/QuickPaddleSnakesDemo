using CSnakes.Runtime;
using Microsoft.Extensions.DependencyInjection;
using Microsoft.Extensions.Hosting;

var appFolder = Path.Join(Environment.CurrentDirectory, "python");

var builder = Host.CreateDefaultBuilder(args)
    .ConfigureServices(services =>
    {
        services
            .WithPython()
            .WithHome(appFolder)
            .WithVirtualEnvironment(Path.Combine(appFolder, ".venv"))
            .FromRedistributable("3.12");
    });
var app = builder.Build();
var env = app.Services.GetRequiredService<IPythonEnvironment>();

var paddleOcr = env.PaddleOcr();
paddleOcr.Predict();