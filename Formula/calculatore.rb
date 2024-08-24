class Calculatore < Formula
  desc "A simple command-line (Italian) calculator"
  homepage "https://github.com/doribenba/calculatore.git"
  url "https://github.com/doribenba/calculatore/releases/download/v2/calculatore-1.0.1.tar.gz"
  sha256 "a9f36bc63b477fd94fe1224c0acce502e53ac750878836dfd5fd5f5829dcebd6"

  def install
    bin.install "calculatore_universal" => "calculatore"
    man1.install "calculatore.1"
  end

  test do
    system "#{bin}/calculatore", "--help"
  end
end
